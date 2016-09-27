;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;                  GENERAL SETTINGS                    ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(setq inhibit-startup-message t)
(menu-bar-mode -1)
(tool-bar-mode -1)
(setq show-paren-delay 0)
(show-paren-mode 1)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;                  COSMETIC SETTINGS                   ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(add-to-list 'custom-theme-load-path "~/.emacs.d/themes/")
(set-default-font "DejaVu Sans Mono-9" )
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-faces-vector
   [default bold shadow italic underline bold bold-italic bold])
 '(column-number-mode t)
 '(custom-safe-themes
   (quote
    ("f641bdb1b534a06baa5e05ffdb5039fb265fde2764fbfd9a90b0d23b75f3936b" "4aee8551b53a43a883cb0b7f3255d6859d766b6c5e14bcb01bed572fcbef4328" "4f0f2f5ec60a4c6881ba36ffbfef31b2eea1c63aad9fe3a4a0e89452346de278" "4cf3221feff536e2b3385209e9b9dc4c2e0818a69a1cdb4b522756bcdf4e00a4" "99953b61ecd4c3e414a177934e888ce9ee12782bbaf2125ec2385d5fd732cbc2" "708df3cbb25425ccbf077a6e6f014dc3588faba968c90b74097d11177b711ad1" "705f3f6154b4e8fac069849507fd8b660ece013b64a0a31846624ca18d6cf5e1" "a1289424bbc0e9f9877aa2c9a03c7dfd2835ea51d8781a0bf9e2415101f70a7e" "06f0b439b62164c6f8f84fdda32b62fb50b6d00e8b01c2208e55543a6337433a" "628278136f88aa1a151bb2d6c8a86bf2b7631fbea5f0f76cba2a0079cd910f7d" "bb08c73af94ee74453c90422485b29e5643b73b05e8de029a6909af6a3fb3f58" "1b8d67b43ff1723960eb5e0cba512a2c7a2ad544ddb2533a90101fd1852b426e" "82d2cac368ccdec2fcc7573f24c3f79654b78bf133096f9b40c20d97ec1d8016" default)))
 '(fci-rule-color "#d6d6d6")
 '(initial-scratch-message nil)
 '(vc-annotate-background nil)
 '(vc-annotate-color-map
   (quote
    ((20 . "#c82829")
     (40 . "#f5871f")
     (60 . "#eab700")
     (80 . "#718c00")
     (100 . "#3e999f")
     (120 . "#4271ae")
     (140 . "#8959a8")
     (160 . "#c82829")
     (180 . "#f5871f")
     (200 . "#eab700")
     (220 . "#718c00")
     (240 . "#3e999f")
     (260 . "#4271ae")
     (280 . "#8959a8")
     (300 . "#c82829")
     (320 . "#f5871f")
     (340 . "#eab700")
     (360 . "#718c00"))))
 '(vc-annotate-very-old-color nil))
(setq-default cursor-type 'box) 

(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;                   FILE MODE HOOKS                    ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(add-to-list 'auto-mode-alist '(".zshrc" . sh-mode))
(add-to-list 'auto-mode-alist '(".sh_aliases" . sh-mode))
(add-to-list 'auto-mode-alist '(".sh_env" . sh-mode))
(add-to-list 'auto-mode-alist '("\\.pl$'" . cperl-mode))
(add-to-list 'auto-mode-alist '("\\.py$'" . python-mode))
(add-to-list 'auto-mode-alist '("\\.js$'" . js2-mode))

(add-hook 'prog-mode-hook 'linum-mode)

(add-hook 'c-mode-hook 'column-enforce-mode)
(add-hook 'python-mode-hook 'elpy-mode)
(add-hook 'python-mode-hook 'column-enforce-mode)
(add-hook 'cperl-mode-hook 'column-enforce-mode)
(add-hook 'prolog-mode-hook 'column-enforce-mode)
(add-hook 'tuareg-mode-hook 'column-enforce-mode)
(add-hook 'java-mode-hook 'column-enforce-mode)
(add-hook 'bash-mode-hook 'column-enforce-mode)


;; Terminal Meta key + arrows
(add-hook 'term-setup-hook
	  '(lambda ()
	     (define-key function-key-map "\e[1;3A" [M-up])
	     (define-key function-key-map "\e[1;3B" [M-down])
	     (define-key function-key-map "\e[1;3C" [M-right])
	     (define-key function-key-map "\e[1;3D" [M-left])
	     (define-key function-key-map "\e[1;5A" [C-up])
	     (define-key function-key-map "\e[1;5B" [C-down])
	     (define-key function-key-map "\e[1;5C" [C-right])
	     (define-key function-key-map "\e[1;5D" [C-left])))

;; After init hooks
(add-hook 'after-init-hook
	  (lambda ()
	    (load-theme 'sanityinc-solarized-light)
	    (require 'multi-web-mode)
	    (setq mweb-default-major-mode 'html-mode)
	    (setq mweb-tags 
		  '((php-mode "<\\?php\\|<\\? \\|<\\?=" "\\?>")
		    (js-mode  "<script[^>]*>" "</script>")
		    (css-mode "<style[^>]*>" "</style>")))
	    (setq mweb-filename-extensions '("php" "htm" "html" "ctp" "phtml" "php4" "php5"))
	    (multi-web-global-mode 1)
	    ))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;                   SERVER SETTINGS                    ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; New frame defaults
(setq default-frame-alist '((font . "DejaVu Sans Mono-9")))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;                MELPA PACKAGE MANAGER                 ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(require 'package)
(add-to-list 'package-archives
             '("melpa" . "https://melpa.org/packages/") t)
(when (< emacs-major-version 24)
  ;; For important compatibility libraries like cl-lib
  (add-to-list 'package-archives '("gnu" . "https://elpa.gnu.org/packages/")))
(package-initialize)
