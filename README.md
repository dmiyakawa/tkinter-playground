# これはなに

tkinterで色々試すかもしれないので一旦作った

Python 3.12.2 + Tk 8.6 を想定。

## Mac (as of 2024-03-23, Sonoma 14.2.1, Homebrew)

https://qiita.com/saki-engineering/items/92b7ec12ed07338929a3 をもとにして動作確認

```
PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I/usr/local/opt/tcl-tk/include' --with-tcltk-libs='-L/usr/local/opt/tcl-tk/lib -ltcl8.6 -ltk8.6'" pyenv install 3.12.2
```

## 情報源

* https://docs.python.org/ja/3/library/tkinter.html
* https://tkdocs.com/tutorial/firstexample.html
* https://tkdocs.com/tutorial/widgets.html

