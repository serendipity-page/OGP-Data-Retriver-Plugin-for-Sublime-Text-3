# English
## OGP Data Retriver Plugin for Sublime Text 3
### Description of the Code
This is a Python 3 code for "Sublime Text 3" plugin.

When your clipboard has a URL string, this plugin tries to retrive the OGP(Open Graph Protocol) data from the URL, process it, and then insert the string at the current cursor.

#### eg.(As of Feb. 7, 2021)
clipboard string: "`https://github.com/`"

inserted string: "`{{< blogcard title = "GitHub: Where the world builds software" description = "GitHub is where over 56 million developers shape the future of software, together. Contribute to the open source community, manage your Git repositories, review code like a pro, track bugs and feat..." site_name = "GitHub" image = "https://github.githubassets.com/images/modules/site/social-cards/github-social.png" url = "https://github.com/" >}}`"

#### Background
I wrote this specifically for a static site generator [Hugo](https://gohugo.io/) because Hugo's shortcode does not let user retrive external data,
and even though there are enormous workarounds on Internet, none of them seems to me fine.

#### Tweak
```python
shortcode_template = "{{< blogcard %s >}}"
arg_template = '%s = "%s"'
```

You can modify a processed string by changing the above two template strings to for other text editing related to OGP.
Also, you can obtain other OGP attributes by addin attribute name into the following args list.  

```python
args = ["title", "description", "site_name", "image", "url"]
```

### How to Install the Plugin
Download [HugoBlogCard.py](https://github.com/serendipity-page/OGP-Data-Retriver-Plugin-for-Sublime-Text-3/blob/main/HugoBlogCard.py) file to your Sublime Text 3's user directory, in my case(on Mac) /Users/username/Library/Application Support/Sublime Text 3/Packages/User.
Binding Keys from Preferences > Key Bindings – Default menu, like:
```json
[
    { 
        "keys": ["ctrl+alt+b"], "command": "hugoblogcard"
    }
]
```

Note: This command should be called by the name "hugoblogcard" in Sublime Text 3 because of the Class name(see source code)

### Link
+ [My Web site(about learning English from foreign TV shows, written in Japanese)](https://www.serendipity.page/)
+ [Article about this plugin(not yet)]

---

# (Japanese)日本語
## 「Sublime Text 3」向けOGPデータ取得プラグイン
### このプログラムの説明
これは「Sublime Text 3」プラグイン向けのPython 3のプログラムです。

もし、クリップボードにURL文字列が入っているなら、このプラグインはそのURLのOGP(Open Graph Protocol)データを取得し、加工し、そしてその加工文字列を現在カーソルのある場所に挿入します。

#### 例（2021/02/07現在）
クリップボードの文字列: "`https://github.com/`"

挿入される文字列: "`{{< blogcard title = "GitHub: Where the world builds software" description = "GitHub is where over 56 million developers shape the future of software, together. Contribute to the open source community, manage your Git repositories, review code like a pro, track bugs and feat..." site_name = "GitHub" image = "https://github.githubassets.com/images/modules/site/social-cards/github-social.png" url = "https://github.com/" >}}`"

#### 背景
自分は静的サイト生成アプリ[Hugo](https://gohugo.io/)向けにこのプログラムを書きました。というのも、Hugoのショートコードは外部リンク先のデータを参照させてくれず、ネット上には様々な回避策が挙がってますが、どれ一つ良さげに思えなかったからです。

#### 調整
```python
shortcode_template = "{{< blogcard %s >}}"
arg_template = '%s = "%s"'
```

上記２つのテンプレート文字列を変更することで、他のOGPに関連するテキスト編集にこのコマンドを使えるようになります。
そして、他のOGP情報も下記リストに文字列を追加することで取得可能です。
Also, you can obtain other OGP attributes by addin attribute name into args list.  

```python
args = ["title", "description", "site_name", "image", "url"]
```

### このプラグインのインストールの仕方
[HugoBlogCard.py](https://github.com/serendipity-page/OGP-Data-Retriver-Plugin-for-Sublime-Text-3/blob/main/HugoBlogCard.py)を「Sublime Text 3」のユーザーディレクトリーにダウンロードします。マックの私の場合、「/Users/username/Library/Application Support/Sublime Text 3/Packages/User」
メニューからキーをバインドします：プリファレンス > キーバインディング > デフォルトから次のように：
```json
[
    { 
        "keys": ["ctrl+alt+b"], "command": "hugoblogcard"
    }
]
```

注意点：このコマンドは「Sublime Text 3」上では"hugoblogcard"と言う名前で呼び出される必要があります、何故ならクラスの名前がそのようになっているため。

### リンク
+ [海外ドラマの中の英語（私のサイト）](https://www.serendipity.page/)
+ [このプラグインに関する記事(まだ)]
