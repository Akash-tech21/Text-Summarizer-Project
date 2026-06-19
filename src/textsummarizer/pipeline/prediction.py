from textsummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.config.tokenizer_path
        )

        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            self.config.model_path
        )

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = self.model.to(self.device)

    def predict(self, text):

        inputs = self.tokenizer(
            text,
            max_length=512,
            truncation=True,
            return_tensors="pt"
        )

        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        summary_ids = self.model.generate(
            **inputs,
            num_beams=4,
            max_length=128,
            length_penalty=0.8
        )

        prediction = self.tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True
        )

        return prediction