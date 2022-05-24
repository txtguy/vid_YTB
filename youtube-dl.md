## Commits

https://github.com/ytdl-org/youtube-dl/commits/master

Latest (working):

- [2022-05-24 **187a48a**](https://github.com/ytdl-org/youtube-dl/commit/187a48aee29847664e0c4cd80fe90c32e1fb334b)

Latest **verified**:

- [2022-05-19 **c3deca8**](https://github.com/ytdl-org/youtube-dl/commit/c3deca86aedd2d8ab7cd0c596fd68b7aeb7c042d)

## Init

```
sudo apt install ffmpeg

sudo apt install python3-venv
```

## Installation

```sh
python3 -m pip install git+https://github.com/ytdl-org/youtube-dl@187a48aee29847664e0c4cd80fe90c32e1fb334b

python3 -m pip install git+https://github.com/ytdl-org/youtube-dl@c3deca86aedd2d8ab7cd0c596fd68b7aeb7c042d
```

## Running

- List formats: `-F`

```sh
youtube-dl --restrict-filenames -o '%(title)s-%(id)s.f%(format_id)s.%(ext)s' --write-info-json -F URL
```


- BEST video (mp4) & audio (m4a): `-f bestvideo[ext=mp4]+bestaudio[ext=m4a]`

```sh
youtube-dl --restrict-filenames -o '%(title)s-%(id)s.f%(format_id)s.%(ext)s' --write-info-json -f bestvideo[ext=mp4]+bestaudio[ext=m4a] URL
```

## Cookies

- [x] OKAY: https://github.com/ytdl-org/youtube-dl#user-content-how-do-i-pass-cookies-to-youtube-dl

    - [**'Get cookies.txt'** extension for Chrome](https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid)

- [ ] TODO: https://apple.stackexchange.com/questions/349697/how-to-use-youtube-dl-cookies
