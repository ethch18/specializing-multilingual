# Specializing Multilingual Language Models: An Empirical Study

This repo contains code for the paper "Specializing Multilingual
Language Models: An Empirical Study" by Ethan C. Chau and Noah A. Smith,
appearing in the Workshop for Multilingual Representation Learning (MRL) 2021.

Data can be found in a [separate
repository](https://gitlab.com/echau18/specializing-multilingual-data); this is
done for Git optimization.

**Requirements**
* PyTorch 1.7.1
* AllenNLP ([fork](https://github.com/ethch18/allennlp/tree/bd4457431e818cc3650e195a2b65345ee3f7c7e9))
* Other packages/repositories as linked below

## How do I...

### ...do LAPT/TVA/vocabulary creation?
Please see the repository for [`Parsing with Multilingual BERT, a Small Corpus,
and a Small Treebank`](https://github.com/ethch18/parsing-mbert), which in turn
references the [original BERT repository](https://github.com/google-research/bert/).

Vocabularies and pre-sharded data for LAPT/TVA for each of the languages used in
this paper can be found in the data repository.

### ...train a monolingual RoBERTa baseline?
First, train a vocabulary from your data.
```
cd scripts/hf_roberta
python train_vocab.py --corpus $TRAIN_TXT --output-dir $VOCAB_DIR
```

Then, train a model.
```
cd scripts/hf_roberta
python train_model.py --train-file $TRAIN_TXT --output-dir $MODEL_DIR \
    --vocab-dir $VOCAB_DIR
```

### ...evaluate a trained LAPT/TVA/RoBERTa model?
```
cd scripts/eval
python eval_mlm.py --eval-file $VALID_TXT --model-dir $MODEL_DIR [--is-roberta]
```

### ...convert a trained LAPT/TVA model to an PyTorch?
See `scripts/modeling/convert_bert_to_hf.py`, which may incur additional
dependencies depending on your system configuration.

### ...transliterate data?
The scripts for these currently have hardcoded paths for each of the datasts.
Please see all scripts beginning with `transliterate_mhr` and
`transliterate_nfkc_ug` in the `scripts/data` directory.

Due to buffering issues related to corpus size, please use the provided script
to canonicalize Uyghur data, and then directly use the Perl script linked below.
Alternatively, pre-transliterated data is available in the data repository.

NOTE: transliterating Meadow Mari requires `transliterate` (Python package), and
Uyghur transliteration references the Perl script from [Muller et al., 2021](https://github.com/benjamin-mlr/mbert-unseen-languages).

### ...train/evaluate a model?

Please see the scripts `hyak-allennlp-train-v2-base` and
`common-allennlp-eval-v2`.  The referenced config files are in the `config/`
directory, including a rather convoluted pathfinding solution that should
resolve the absolute path of the `mtl.libsonnet` config library file.  The
config files used in the paper are all in `config/autogen/`; should they need to
be regenerated, you can use the `config/lib/configurator_mtl` script.

### ...generate the graphs from the paper?
First, generate a vocabulary report for all the languages in question using
`scripts/vocabulary/analyze_vocabulary.py`.  Then, please see
`scripts/analysis/analyze.py`.

## Citation
Please cite our work if you have found it helpful!
```
@misc{chau2021specializing,
      title={Specializing Multilingual Language Models: An Empirical Study}, 
      author={Ethan C. Chau and Noah A. Smith},
      year={2021},
      eprint={2106.09063},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

If you experiment with TVA and/or transliteration, please also cite the relevant
works:
```
@inproceedings{chau-etal-2020-parsing,
    title = "Parsing with Multilingual {BERT}, a Small Corpus, and a Small Treebank",
    author = "Chau, Ethan C.  and
      Lin, Lucy H.  and
      Smith, Noah A.",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.118",
    doi = "10.18653/v1/2020.findings-emnlp.118",
}
```

```
@inproceedings{muller-etal-2021-unseen,
    title = "When Being Unseen from m{BERT} is just the Beginning: Handling New Languages With Multilingual Language Models",
    author = "Muller, Benjamin  and
      Anastasopoulos, Antonios  and
      Sagot, Beno{\^\i}t  and
      Seddah, Djam{\'e}",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.38",
    doi = "10.18653/v1/2021.naacl-main.38",
}
```
