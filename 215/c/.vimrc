" Vim wellcome
autocmd VimEnter * echo "_eo to quickly go to config file"
let mapleader=" "

" Pretty the view
color darkblue
nnoremap <leader>on :set invnumber<CR>
nnoremap <leader>or :set invrelativenumber<CR>
set cursorline
set number

" Setup c compiler, debuger(?)
" set makeprg=gcc\ -I.\ -o\ dist/%:r\ %\ -fdiagnostics-color
" set errorformat=%D
" Toggle quickfix window

function! ToggleQuickfix()
    if empty(filter(getwininfo(), 'v:val.quickfix'))
        copen
    else
        cclose
    endif
endfunction

nnoremap <silent> <leader>di :call ToggleQuickfix()<CR>
nnoremap <silent> <leader>dn :colder<CR>
nnoremap <silent> <leader>dN :cnewer<CR>
nnoremap <silent> [d :cn<CR>
nnoremap <silent> ]d :cp<CR>



" Jumping
nnoremap <C-u> <C-u>zz
nnoremap <C-d> <C-d>zz

" Quick jump buffer
nnoremap <leader>bn :bnext<CR>
nnoremap <leader>bN :bprevious<CR>
nnoremap <leader>bd :bdelete<CR>
set switchbuf=useopen

" Window management
nnoremap <leader>wa :ball<CR>

" Map [d to :cnext (next error)
" nnoremap [d :cnext<CR>

" Map ]d to :cprev (previous error)
" nnoremap ]d :cprev<CR>

" Config management
nnoremap <leader>vpp :e $MYVIMRC<cr>
nnoremap <leader>eo :e $MYVIMRC<cr>
nnoremap <leader><leader> :source ~/.vimrc<CR>
nnoremap <F5> :make<CR>

" Format
" Use spaces instead of tabs
set expandtab

" Set tab width to 4 spaces
set tabstop=4
set shiftwidth=4
" Auto indent on new line
set autoindent
set smartindent

" Vim defaul format
nnoremap <leader>f mlGVgg=`l

" Explore
nnoremap <leader>pv :Explore %:p:h<CR>

" Define a custom command <leader>pf for finding files in the CWD
command -nargs=1 FindFiles call FindFiles(<q-args>)

function FindFiles(pattern)
    let filelist = split(glob(getcwd() . '/' . a:pattern), "\n")
    if empty(filelist)
    echomsg 'No files found matching: ' . a:pattern
    else
        call setqflist(map(filelist, '{ "filename": v:val }'))
        copen
        echomsg len(filelist) . ' files found.'
    endif
endfunction

nnoremap <silent> <leader>pf :call FindFiles(input("Find files: "))<CR>

" Open last/recent change buffer
nnoremap <leader>pr `0
nnoremap <leader>pr0 `0
nnoremap <leader>pr1 `1
nnoremap <leader>pr2 `2
nnoremap <leader>pr3 `3
nnoremap <leader>pr4 `4
