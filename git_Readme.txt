�������ݒ�
---------------------------------------------------
git config --global user.name "****"
git config --global user.email "*****@gmail.com"
git config --global core.editor "'c:\Program Files\Hidemaru\Hidemaru.exe' -CODE=4"
git config --list


�����s�R�}���h
---------------------------------------------------
git init
git status
git log			':'�̂Ƃ���� q �L�[�������ƒ��f
git add .
git add git_Readme.txt
git commit -m 'first commit'


��GitHub / 8.push:�X�V��uplaod
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
git push �v�b�V���� ���[�J���̃u�����`�� :�����[�g�̃u�����`��

��GitHub / 9.pull:����download
---------------------------------------------------
git remote add origin https://github.com/vitalis-noah/Tutorial-git.git
git pull origin master
- - - - - - - - - - - - - - - - - - -
git pull origin master


��GitHub / 10.clone:�S�t�@�C��������download 
---------------------------------------------------
git clone https://github.com/vitalis-noah/Tutorial-git.git


��GitHub / 11.branch:
---------------------------------------------------
git branch	:���[�J��(PC)�̃u�����`�ꗗ
git branch -r	:�����[�g(GitHub)�̃u�����`�ꗗ
git branch -a	:���[�J���A�����[�g�����̃u�����`�ꗗ
- - - - - - - - - - - - - - - - - - -
git branck '�u�����`�̖��O'	 :�u�����`�̍쐬
git checkout �u�����`�̖��O	 :�u�����`�̐؂�ւ�
git checkout -b '�u�����`�̖��O' :�u�����`�̍쐬�Ɛ؂�ւ�
- - - - - - - - - - - - - - - - - - -
git branch -d �u�����`�̖��O	:�u�����`�̍폜
git branch -m '�u�����`��'	:�u�����`���̕ύX
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


��GitHub / 12. Remote Branch: �����[�g�Ƀu�����`��o�^
---------------------------------------------------
git push -u origin �쐬�����u�����`��		:�u�����`�������[�g�ɓo�^
git branch ���[�J���ɍ쐬����u�����`�� origin  :�����[�g�u�����`���烍�[�J���u�����`���쐬
- - - - - - - - - - - - - - - - - - -
git push -u origin second
- - - - - - - - - - - - - - - - - - -
git push	: -u�I�v�V�����œo�^��́A�����OK


��GitHub / 13. merge:�u�����`�𓝍�
---------------------------------------------------
git merge ��荞�ރu�����`��
- - - - - - - - - - - - - - - - - - -
git checkout master	:�@ master�ɂ��Ă���
git merge second	:�A ��荞�ރu�����`�����w�肵�ē���
git push		:�B �����[�g�ɓo�^


��GitHub / 14. Fetch:�����[�g����ŐV���������Ă���
---------------------------------------------------
git fetch
- - - - - - - - - - - - - - - - - - -
pull = Fetch + Merge 	 : pull�Ƃ̈Ⴂ,Fetch�� ����Ă��邾��
git merge origin/master	 : ��ŁAmerge������K�v������.(merge�͎��Ԃ�������)
- - - - - - - - - - - - - - - - - - -
git fetch
git status
git merge origin/master
- - - - - - - - - - - - - - - - - - -
clone : �����[�g�̓��e��S�����[�J���ɂ����Ă���
pull  : �����̂݃��|�W�g����������Ă���{�������s���A�}�X�^���X�V�����
fetch : �����̂݃��|�W�g����������Ă���B�}�X�^�̍X�V�͌�� ������(git merge origin/master)����K�v������



��GitHub / 15. Rebase : master�̍ŐV�����u�����`�ɔ��f����(master�̍X�V�͂��Ȃ��j����肪�Ȃ���� maerge���s��
---------------------------------------------------

��GitHub / 16. Fork : ���̃A�J�E���g�̃��|�W�g���������̃A�J�E���g�ɃR�s�[
��GitHub / 16. Pull Request : �R�s�[���Ă������|�W�g����ύX���ăI���W�i���� pull��v������
---------------------------------------------------
GitHub��HomePage�� Fork�̃{�^������B���̃A�J�E���g�̃v���W�F�N�g���Ђ炢����ԂŁA�{�^���������ƁA
�����̃A�J�E���g�ɃR�s�[���Ă����


��GitHub / 17. �C�ӂ̏ꏊ�ɖ߂�
---------------------------------------------------
git reset HEAD^

--hard		: HEAD(commit), �C���f�b�N�X(Add), �t�@�C���ύX(���[�L���O�c���[) �S�Ė߂�
--mixed		: HEAD(commit), �C���f�b�N�X(Add) �̂Q��߂�
--soft		: HEAD(commit) �̂ݖ߂�

git reset --soft HEAD^	: 1�܂��ɖ߂�

HEAD^^^	: 3�O�ɖ߂�
HEAD~3
@^^^
- - - - - - - - - - - - - - - - - - -
git reset --hard HEAD^
git reset --soft HEAD^

