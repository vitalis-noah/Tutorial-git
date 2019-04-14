■初期設定
---------------------------------------------------
git config --global user.name "****"
git config --global user.email "*****@gmail.com"
git config --global core.editor "'c:\Program Files\Hidemaru\Hidemaru.exe' -CODE=4"
git config --list


■実行コマンド
---------------------------------------------------
git init
git status
git log			':'のところで q キーを押すと中断
git add .
git add git_Readme.txt
git commit -m 'first commit'


■GitHub / 8.push:更新をuplaod
---------------------------------------------------
echo "# Tutorial-git" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/vitalis-noah/Tutorial-git.git
git push -u origin master
- - - - - - - - - - - - - - - - - - -
git remote add origin https://github.com/vitalis-noah/Tutorial-git.git
git push -u origin master
- - - - - - - - - - - - - - - - - - -
git push
- - - - - - - - - - - - - - - - - - -
git push プッシュ先 ローカルのブランチ名 :リモートのブランチ名

■GitHub / 9.pull:差分download
---------------------------------------------------
git remote add origin https://github.com/vitalis-noah/Tutorial-git.git
git pull origin master
- - - - - - - - - - - - - - - - - - -
git pull origin master


■GitHub / 10.clone:全ファイル＆履歴download 
---------------------------------------------------
git clone https://github.com/vitalis-noah/Tutorial-git.git


■GitHub / 11.branch:
---------------------------------------------------
git branch	:ローカル(PC)のブランチ一覧
git branch -r	:リモート(GitHub)のブランチ一覧
git branch -a	:ローカル、リモート両方のブランチ一覧
- - - - - - - - - - - - - - - - - - -
git branck 'ブランチの名前'	 :ブランチの作成
git checkout ブランチの名前	 :ブランチの切り替え
git checkout -b 'ブランチの名前' :ブランチの作成と切り替え
- - - - - - - - - - - - - - - - - - -
git branch -d ブランチの名前	:ブランチの削除
git branch -m 'ブランチ名'	:ブランチ名の変更
- - - - - - - - - - - - - - - - - - -
git branch
git branch -r
git branch -a
git branch 'second'
git checkout second
git branch
git add .
git commit -m 'second branch first commit'
git status
git checkout master
git checkout second


■GitHub / 12. Remote Branch: リモートにブランチを登録
---------------------------------------------------
git push -u origin 作成したブランチ名		:ブランチをリモートに登録
git branch ローカルに作成するブランチ名 origin  :リモートブランチからローカルブランチを作成
- - - - - - - - - - - - - - - - - - -
git push -u origin second
- - - - - - - - - - - - - - - - - - -
git push	: -uオプションで登録後は、これでOK


■GitHub / 13. merge:ブランチを統合
---------------------------------------------------
git merge 取り込むブランチ名
- - - - - - - - - - - - - - - - - - -
git checkout master	:① masterにしておく
git merge second	:② 取り込むブランチ名を指定して統合
git push		:③ リモートに登録


■GitHub / 14. Fetch:リモートから最新情報を持ってくる
---------------------------------------------------
git fetch
- - - - - - - - - - - - - - - - - - -
pull = Fetch + Merge 	 : pullとの違い,Fetchは 取ってくるだけ
git merge origin/master	 : 後で、mergeをする必要がある.(mergeは時間がかかる)
- - - - - - - - - - - - - - - - - - -
git fetch
git status
git merge origin/master
- - - - - - - - - - - - - - - - - - -
clone : リモートの内容を全部ローカルにもってくる
pull  : 差分のみリポジトリからもってくる＋統合も行い、マスタも更新される
fetch : 差分のみリポジトリからもってくる。マスタの更新は後で 自分で(git merge origin/master)する必要がある



■GitHub / 15. Rebase : masterの最新情報をブランチに反映する(masterの更新はしない）→問題がなければ maergeを行う
---------------------------------------------------

■GitHub / 16. Fork : 他のアカウントのリポジトリを自分のアカウントにコピー
■GitHub / 16. Pull Request : コピーしてきたリポジトリを変更してオリジナルに pullを要請する
---------------------------------------------------
GitHubのHomePageに Forkのボタンがる。他のアカウントのプロジェクトをひらいた状態で、ボタンを押すと、
自分のアカウントにコピーしてくれる


■GitHub / 17. reset :任意の場所に戻る（履歴も取消）
---------------------------------------------------
git reset HEAD^

--hard		: HEAD(commit), インデックス(Add), ファイル変更(ワーキングツリー) 全て戻す
--mixed		: HEAD(commit), インデックス(Add) の２つを戻す
--soft		: HEAD(commit) のみ戻す

git reset --soft HEAD^	: 1つまえに戻る

HEAD^^^	: 3つ前に戻る
HEAD~3
@^^^
- - - - - - - - - - - - - - - - - - -
git reset --hard HEAD^
git reset --soft HEAD^


■GitHub / 18. revert : commitを取り消すcommitを実行（履歴が残る/安全）
---------------------------------------------------
git revert HEAD
- - - - - - - - - - - - - - - - - - -
git log
git revert e0d014f425f3481591daf1cfad96bd5de1e7405e
git log


■GitHub / 20. GitIgnore : Gitの管理に含めないファイルを指定
---------------------------------------------------
.gitignoreファイルを作成

#で始まる行はコメントとして扱われる

*.exe			:*.exe拡張子
bin/			:特定のフォルダ
package/**/*.ts		:特定のフォルダの.ts拡張子
- - - - - - - - - - - - - - - - - - -
windowsでは .gitignore のファイルは作れない（ファイル名をいれてください）
そこで...
gitignore.txt をつくり、dosプロンプト(エクスプローラのアドレスに cmd とすれば dosが起動)で rename する

c:\***\**\**>ren gitignore.txt .gitignore

または...
.gitignore.txt というファイルをつくり、エクスプローラで
.gitignore. に名前を変更する（警告がでるがOKとする）
