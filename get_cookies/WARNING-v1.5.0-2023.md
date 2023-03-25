
[2023-01-13] https://www.reddit.com/r/youtubedl/comments/10ar7o7/if_youve_been_using_the_get_cookiestxt_chrome/

----

## If you've been using the "Get cookies.txt" Chrome extension, it's tracking you now.

** [Update from 2023-03-04: The situation is now even worse; the extension
is [now also sending all your cookies to the developer, too](https://old.reddit.com/r/youtubedl/comments/11i5vyq/psa_the_get_cookiestxt_extension_is_now_actively/).]**


The "Get cookies.txt" extension updated to version `1.5.0` yesterday
and the new update is sending details of **every** page you visit
(not just video sites, but every page)
back to its developer at the domain "ck.getcookiestxt.com".

Specifically, for every page you visit, it sends:
- The page address,
- A unique ID for your browser installation,
- Your browser's user-agent string (which shows what OS you're using and the browser version number),
- Your language setting,
- The platform you're on,
- The current date/time and your current timezone.

I'd highly recommend moving away from this extension ASAP.

Now for the good news: If you're using `yt-dlp`, you don't need to use this extension!
It has a `--cookies-from-browser` switch which allows you to say, for example,
`--cookies-from-browser firefox` and it'll get the cookies directly from your browser.
There are also advanced usages that allow you to specify decryption keyrings,
profile paths, and (for Firefox) container names - see the `yt-dlp --help` output for details.

Please be careful out there!

----
