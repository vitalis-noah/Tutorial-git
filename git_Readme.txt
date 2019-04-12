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
git log
git add .
git add git_Readme.txt
git commit -m 'first commit'


■GitHub / push
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

■GitHub / pull
---------------------------------------------------
git remote add origin https://github.com/vitalis-noah/Tutorial-git.git
git pull origin master
- - - - - - - - - - - - - - - - - - -
git pull origin master


