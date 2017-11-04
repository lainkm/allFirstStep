" a插入，o插入行 大写i是行首插入，ijkl上下左右
" 全选，复制，粘贴
" 新建窗口ctrl-n
" 注释 ctrl-v选择行首 大写的i进入插入模式，
" 然后键入# 或者// 或者"
" 最后按两下esc，就可以注销了，取消的话直接进入visual选上，再d就行
" 分屏 :vs :sv + filename
" 切换 ctrl+w 切换下一个，ctrl + ikjl是上下左右

set nocompatible
autocmd BufWritePost $MYVIMRC source $MYVIMRC    "让配置立即生效
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'tmhedberg/SimpylFold' "折叠
Plugin 'vim-scripts/indentpython.vim' "缩进
Plugin 'scrooloose/syntastic'   "缩进
Plugin 'nvie/vim-flake8'  "检查语法高亮
Plugin 'scrooloose/nerdtree' 
Plugin 'jistr/vim-nerdtree-tabs' "文件树
Plugin 'kien/ctrlp.vim' "搜索全部文件
Plugin 'tpope/vim-fugitive' "git集成
Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
call vundle#end()


let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree
let g:SimpylFold_docstring_preview=1  "希望看到折叠代码的文档字符串
" 缩进
""au BufNewFile,BufRead *.py
\ set tabstop=4
\ set softtabstop=4
\ set shiftwidth=4
\ set textwidth=79
\ set expandtab
\ set autoindent
\ set fileformat=unix
""au BufNewFile,BufRead *.js, *.html, *.css
\ set tabstop=2
\ set softtabstop=2
\ set shiftwidth=2
" 将多余的空白字符高亮显示
""au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/
let python_highlight_all=1
syntax on









set syntax=on   "语法高亮
set nu
syntax enable
syntax on
set go=
set ruler
set showcmd
set scrolloff=3
set laststatus=1
set foldenable
set foldmethod=manual "手动折叠
"空格代替za进行折叠
nnoremap <space> za  
set tabstop=4
set background=dark
set nocompatible     
colorscheme murphy   "配色方案
set fencs=utf-8,ucs-bom,shift-jis,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set enc=utf-8
set fencs=utf-8,ucs-bom,shift-jis,gb18030,gbk,gb2312,cp936
set langmenu=zh_CN.UTF-8
set helplang=cn
set encoding=utf-8
set fileencodings=ucs-bom,utf-8,cp936
set fileencoding=utf-8
filetype plugin on "允许使用插件
set autoread "文件被改动时自动载入
autocmd FileType c,cpp,py map <buffer> <leader><space> :w<cr>:make<cr>
set completeopt=preview,menu  "代码补全
set clipboard=unnamed  "共享剪贴板
set nobackup "从不备份
:set makeprg=g++\ -Wall\\%  "make运行
set autowrite " 自动保存
set cursorline "游标显示当前行
set magic
set guioptions-=T "隐藏工具栏
set guioptions-=m "隐藏菜单栏
set foldcolumn=0  "设置在状态行显示信息
set foldmethod=indent 
set foldlevel=3 
set foldenable   
set noeb  "去掉输入错误的提示音
set confirm "在处理未保存或只读文件的时候，弹出确认
set autoindent
set cindent
set smartindent
set tabstop=4
set softtabstop=4
set shiftwidth=4
set smarttab
set noexpandtab
set number
set history=1000
set nobackup
set noswapfile
set ignorecase "搜索忽略大小写
set hlsearch
set incsearch "搜索字符高亮
set gdefault "行内替换
set backspace=2
set whichwrap+=<,>,h,l "允许光标跨行
set mouse=a
set selection=exclusive
set selectmode=mouse,key "鼠标
set report=0  "通过：commands知道那一行被该过 ?
set fillchars=vert:\ ,stl:\ ,stlnc:\  "在被分割的窗口间显示空白，便于阅读
set showmatch "高亮括号匹配
set matchtime=1 "高亮匹配时间0.1秒
set scrolloff=3
map <C-A> ggVG
map! <C-A> <Esc>ggVG
map <F12> gg=G
vmap <C-c> "+y
vmap <C-v> "+p
map <C-n> :tabnew<CR> 
map <F3>:tabnew .<CR>
map <C-F3> \be
map <F5>:call CompileRunGcc()<CR>
"映射上下左右的光标移动  
nnoremap  i   k  
nnoremap  k   j  
nnoremap  j   h
nnoremap  a   i
nnoremap <C-K> <C-W><C-J>
nnoremap <C-I> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-J> <C-W><C-H>
"行光标移动  
nmap J   ^  
nmap L  $ 
""imap <C+s> <ESC>:w<CR>a  "不能用ctrl+s保存被系统占用
func! CompileRunGcc()
    exec "w"
    if &filetype == 'c'
		exec "!g++ % -o %<"
        exec "! ./%<"
    elseif &filetype == 'cpp'
        exec "!g++ % -o %<"
        exec "! ./%<"
    elseif &filetype == 'java' 
        exec "!javac %" 
        exec "!java %<"
    elseif &filetype == 'sh'
        :!./%
    elseif &filetype == 'py'
	exec "!python %"
    endif
endfunc

"自动补全
:inoremap ( ()<ESC>i
:inoremap ) <c-r>=ClosePair(')')<CR>
:inoremap { {<CR>}<ESC>O
:inoremap } <c-r>=ClosePair('}')<CR>
:inoremap [ []<ESC>i
:inoremap ] <c-r>=ClosePair(']')<CR>
:inoremap " ""<ESC>i
:inoremap ' ''<ESC>i
function! ClosePair(char)
	if getline('.')[col('.') - 1] == a:char
		return "\<Right>"
	else
 		return a:char
	endif
endfunction
filetype plugin indent on 
"开文件类型检测, 加了这句才可以用智能补全
set completeopt=longest,menu

"CTages设定
let Tlist_Sort_Type = "name"    " 按照名称排序  
let Tlist_Use_Right_Window = 1  " 在右侧显示窗口  
let Tlist_Compart_Format = 1    " 压缩方式  
let Tlist_Exist_OnlyWindow=1  "如果只有一个buffer，kill窗口也kill掉buffer  
let Tlist_File_Fold_Auto_Close = 0  " 不要关闭其他文件的tags  
let Tlist_Enable_Fold_Column = 0    " 不要显示折叠树  
autocmd FileType java set tags+=D:\tools\java\tags 
autocmd FileType h,cpp,cc,py,c set tags+=D:\tools\cpp\tags  
let Tlist_Show_One_File=1  "不同时显示多个文件的tag，只显示当前文件的
set tags=tags  
let Tlist_Auto_Open=1 
""#
""#leader就是#，使用的时候就是#w是保存，为了避免二义性"
""#let mapleader="#"
""#nmap <leader>w    :w<CR> 
