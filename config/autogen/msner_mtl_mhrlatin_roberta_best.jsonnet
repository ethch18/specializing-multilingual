local t = import "DO_NOT_ERASE_pathfinder.libsonnet";

t.build_mtl_ner_ms("mhrlatin", "bert", ["roberta", "best"], "mtl_mhrlatin_roberta_best")
