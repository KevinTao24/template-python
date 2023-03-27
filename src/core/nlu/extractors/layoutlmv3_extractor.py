from typing import Optional, Text

import torch
from transformers import (
    LayoutLMv3ForTokenClassification,
    LayoutLMv3Processor,
    Trainer,
    TrainingArguments,
)


class LayoutLMv3Extractor:
    DEFAULT = {
        "epochs": 3,
        "batch_size": 8,
        "learning_rate": 3e-5,
        "weight_decay": 0.01,
    }

    def __init__(self, model_path: Optional[Text] = None):
        self.model_path = model_path
        self.model = None
        self.processor = None

    @staticmethod
    def process_data(data):
        """Process the input data and return the processed data.

        Args:
            data (_type_): A dictionary containing the input data with keys "tokens" and "image_path" (optional).

        Returns:
            _type_: A dictionary with the processed data.
        """

        if "tokens" not in data:
            raise ValueError("The input data should contain 'tokens' field.")

        tokens = data["tokens"]
        image_path = data.get("image_path", None)

        inputs = {
            "input_ids": tokens["input_ids"],
            "attention_mask": tokens["attention_mask"],
        }
        if image_path:
            inputs["image"] = image_path

        inputs["labels"] = tokens["input_ids"]
        del inputs["input_ids"], inputs["image"]
        return inputs

    def train(
        self,
        train_dataset,
        val_dataset,
        epochs: Optional[int] = None,
        batch_size: Optional[int] = None,
        learning_rate: Optional[float] = None,
        weight_decay: Optional[float] = None,
        save_path: Optional[Text] = None,
    ):
        """Train the model with the given dataset and hyperparameters.

        Args:
            train_dataset (_type_): The dataset used for training.
            val_dataset (_type_): The dataset used for validation.
            epochs (Optional[int], optional): The number of epochs to train for. Default is 3.
            batch_size (Optional[int], optional): The size of the mini-batches. Default is 8.
            learning_rate (Optional[float], optional): The learning rate for the optimizer. Default is 3e-5.
            weight_decay (Optional[float], optional): The weight decay for the optimizer. Default is 0.01.
            save_path (Optional[Text], optional): The path to save the trained model and processor. Default is None.
        """

        epochs = epochs if epochs else self.DEFAULT["epochs"]
        batch_size = batch_size if batch_size else self.DEFAULT["batch_size"]
        learning_rate = (
            learning_rate if learning_rate else self.DEFAULT["learning_rate"]
        )
        weight_decay = weight_decay if weight_decay else self.DEFAULT["weight_decay"]

        self.model_path = self.model_path or "output"
        self.model = LayoutLMv3ForTokenClassification.from_pretrained(self.model_path)
        self.processor = LayoutLMv3Processor.from_pretrained(self.model_path)

        train_dataset = train_dataset.map(self.process_data, batched=True)
        val_dataset = val_dataset.map(self.process_data, batched=True)

        training_args = TrainingArguments(
            output_dir=self.model_path,
            num_train_epochs=epochs,
            per_device_train_batch_size=batch_size,
            per_device_eval_batch_size=batch_size,
            evaluation_strategy="epoch",
            save_strategy="epoch",
            logging_dir="logs",
            learning_rate=learning_rate,
            weight_decay=weight_decay,
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=val_dataset,
        )

        trainer.train()

        if save_path:
            self.save(save_path)

    def process(self, image_path: Text, tokens):
        """Process the image and tokens and return predictions.

        Args:
            image_path (Text): The path of the image file.
            tokens (_type_): The list of tokenized text.

        Returns:
            _type_: A list of predictions.
        """

        inputs = self.processor(
            image_path, tokens, padding="max_length", return_tensors="pt"
        )
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            predictions = torch.argmax(logits, dim=2)

        return predictions.tolist()[0]

    def save(self, save_path: Text):
        """Save the trained model and processor to the specified path.

        Args:
            save_path (Text): The path to save the model and processor.
        """

        self.model.save_pretrained(save_path)
        self.processor.save_pretrained(save_path)

    @classmethod
    def from_pretrained(cls, model_path: Text):
        """Load a pretrained model and processor from the specified path.

        Args:
            model_path (Text): The path to the pretrained model and processor.

        Returns:
            _type_: An instance of LayoutLMv3NER with the loaded model and processor.
        """

        extractor = cls()
        extractor.model_path = model_path
        extractor.model = LayoutLMv3ForTokenClassification.from_pretrained(model_path)
        extractor.processor = LayoutLMv3Processor.from_pretrained(model_path)

        return extractor


if __name__ == "__main__":
    from datasets import load_dataset

    train_dataset = load_dataset("my_dataset", split="train")
    val_dataset = load_dataset("my_dataset", split="validation")

    train_extractor = LayoutLMv3Extractor(model_path="my_pretrained_model")
    save_path = "output"
    train_extractor.train(train_dataset, val_dataset, save_path=save_path)

    extractor = LayoutLMv3Extractor.from_pretrained(save_path)

    image_path = "path/to/your/image.png"
    tokens = ["token1", "token2", "token3"]
    predictions = extractor.process(image_path, tokens)

    print(predictions)
