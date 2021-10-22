import argparse
import os

from transformers import (
    BertTokenizerFast,
    BertForMaskedLM,
    DataCollatorForLanguageModeling,
    LineByLineTextDataset,
    RobertaTokenizerFast,
    RobertaForMaskedLM,
    TrainingArguments,
    Trainer,
)

parser = argparse.ArgumentParser()
parser.add_argument("--eval-file", type=str, required=True)
parser.add_argument("--model-dir", type=str, required=True)
parser.add_argument("--is-roberta", action="store_true")
parser.add_argument("--mlm-probability", type=float, default=0.15)
args = parser.parse_args()

results = {}

for i in range(1, 21):
    dir = os.path.join(args.model_dir, f"epoch_{i}")
    if not os.path.exists(dir):
        continue

    if args.is_roberta:
        tokenizer = RobertaTokenizerFast.from_pretrained(dir, max_len=512)
        model = RobertaForMaskedLM.from_pretrained(dir)

    else:
        tokenizer = BertTokenizerFast.from_pretrained(
            dir,
            clean_text=True,
            tokenize_chinese_chars=True,
            strip_accents=False,
            do_lower_case=False,
        )
        model = BertForMaskedLM.from_pretrained(dir)

    dataset = LineByLineTextDataset(
        tokenizer=tokenizer, file_path=args.eval_file, block_size=128
    )
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, mlm=True, mlm_probability=args.mlm_probability
    )

    training_args = TrainingArguments(
        output_dir=".",
        per_device_eval_batch_size=32,
        do_train=False,
        do_eval=True,
    )
    trainer = Trainer(
        model=model,
        args=training_args,
        eval_dataset=dataset,
        data_collator=data_collator,
    )
    metrics = trainer.evaluate()
    results[i] = metrics

print(results)
