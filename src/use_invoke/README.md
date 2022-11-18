# run invoke

invokeをタスクランナーとして利用するサンプルです。
正直pythonスクリプトを用意したほうが便利だと思います。

```bash
./pants run src/use_invoke:invoke --run-args="hello"
```

```bash
./pants run src/use_invoke:invoke --run-args="hello --name=hoge"
```
