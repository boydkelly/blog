+++
author = "Boyd Kelly"
date = 2020-04-13T00:00:00Z
description = ""
featured_image = ""
lang = "en"
subjects = ["technologie"]
tags = ["tech, french, "]
title = "Easy French style punctuation with NVIM/VIM"

+++
Are you often having to type in English and in French like me? If so how are you 
managing the French requirment for a space before the question mark and exlamation mark?  Obligatory in French but horrendous in English!

This is easy to look after with my preferred text editor NVIM:

Create a file at the following location for either vim/gvim or nvim:

(vim/gvim): .vim/keymap/fr.vim (vim/gvim) 
(nvim) .local/share/nvim/site/keymap/fr.vim 

with this simple content: 
    
    let b:keymap_name="french punctuation"
    
    highlight lCursor ctermbg=red guibg=red
    
    loadkeymap
    
    ?  <space>?
    !  <space>!
    
that automatically adds a space before any question mark or exclamation mark.

To activate the keymap, type:

:set keymap=fr

To deactivate the keymap, type:

:set keymap=

Allez-vous esseyer ?  Formidable !
Will you try?  Awesome!
