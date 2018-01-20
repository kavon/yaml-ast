# yaml-ast
visualize an AST serialized as YAML

### Requirements

You need PyYAML and GraphViz installed.

```
sudo pip install pyyaml
brew install graphviz
```

### Usage

```
python show.py ast.yaml > graph.gv
dot -Tpdf graph.gv -o render.pdf
```
