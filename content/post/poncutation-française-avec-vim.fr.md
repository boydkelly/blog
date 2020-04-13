+++
author = "Boyd Kelly"
date = 2020-04-13T00:00:00Z
description = ""
featured_image = ""
marques = []
sujets = []
title = "Poncutation française avec VIM"

+++
Si vous avez l'habitude de tapper en anglais et en français, comme moi, comment gérez-vous les espaces qui précedent les points d'interrogation et d'exclamation ?  En français, selon les normes (??  en tout cas), il faut avoir des espaces, mais les anglais sont horrifiés de voir cela.

Avec mon éditeur préféré NVIM sous linux c'est chose façile:

Creer un ficher à l'endroit suivant pour soit vim/gvim ou bien nvim

(vim/gvim): .vim/keymap/fr.vim (vim/gvim) 
(nvim) .local/share/nvim/site/keymap/fr.vim 

Avec le contenu très simple suivant: 
    
    let b:keymap_name="french punctuation"
    
    highlight lCursor ctermbg=red guibg=red
    
    loadkeymap
    
    ?  <space>?
    !  <space>!
    
qui met automatiquement une espace devant les deux signes.

Pour activer le ficher tappez:

:set keymap=fr

Pour désactiver tappez:

:set keymap=

Allez-vous esseyer ?  Formidable !