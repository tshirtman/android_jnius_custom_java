### Custom java code in Kivy/P4A app built with buildozer

To test the app on desktop (before building for android), you can run.

```sh
ant all
python app/main.py
```

To test on android, make sure you have buildozer installed and functionnal and run.

```sh
buildozer android debug deploy run logcat
```

This repository uses github actions to produce an apk you can download and run.
