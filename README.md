# codekitty library

## Major Changes

- this will be for cpx
- no longer need to include a lib folder
- used cpx lib which replaces simpleio and board
- broke out sounds to another lib


## Guidelines 

- To add features, create a feature branch then pull request to merge with master. Example git comands:
```
git checkout -b "feature/rainbow"
git checkout -b "fix/cpx4.0"
git checkout -b "experimental/turret"
git checkout -b "board/trinketM0"
```
- Master branch corresponds to whatever the most current kitty is using
- Maintain a branch for each other board
- Create releases for each board until we no longer support a board
- Use semantic versioning for releases
- No versioning in master
- https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases
- https://github.com/adafruit/circuitpython
- https://github.com/adafruit/circuitpython/releases
- https://semver.org/