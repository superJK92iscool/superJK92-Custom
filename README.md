# superJK92-Custom

[![Build JAR](https://github.com/superJK92iscool/superJK92-Custom/actions/workflows/build.yml/badge.svg)](https://github.com/superJK92iscool/superJK92-Custom/actions/workflows/build.yml)

<img src="https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/fd/Firework_Rocket_JE2_BE2.png" alt="firework_rocket" width="16"/> superJK92-Custom is a new Firework-based server software derived from Paper, Purpur, and several other forks. Firework un-patches many controversial changes introduced in upstream server softwares, such as duplication patches and changes to mob spawning behaviors. superJK92-Custom aims to restore vanilla-like behavior while maintaining the excellent performance gains introduced by Spigot and Paper. It also preserves the extreme customizability introduced with Purpur. We sincerely hope you enjoy playing on superJK92-Custom as much as we enjoy developing it!

Firework is developed in collaboration with [nota-noob](https://github.com/nota-noob) for the Outcast SMP.
And superJK92-Custom was "made" by [superJK92](https://github.com/superJK92iscool)
## Downloads
#### Stable
We recommend grabbing the stable server JAR for superJK92-Custom from [GitHub Releases](https://github.com/superJK92iscool/superJK92-Custom/releases).
#### Bleeding-Edge
If you'd like to live on the bleeding-edge of superJK92-Custom development, grab the server JAR from [GitHub Actions](https://github.com/superJK92iscool/superJK92-Custom/actions). **These versions are not be extensively tested and may contain server-breaking bugs!**

## Contributing
#### Issues
If you found a bug, performance problem, or the server JAR crashes, please report file an issue report on [Github Issues](https://github.com/superJK92iscool/superJK92-Custom/issues). If you'd like your issue to be resolved as fast as possible, please include all information relevant to your issue.

#### Pull Requests
We welcome all pull requests! Please make sure that your pull request adds a feature or solves an issue. Pull requests linked with issues are especially appreciated!

#### Compiling
Patches are server extensions, which can be found in the `/patches` directory.

To generate your own JAR from superJK92-Custom's source code, run these commands in the root directory of your downloaded superJK92-Custom folder:
```
./gradlew applyPatches
./gradlew build
./gradlew createReobfPaperclipJar
```
The generated JAR file should be located in the `/build/libs` directory and should end with `-paperclip-*.jar`. You can either point your launch script to this new JAR or rename it to something else, such as `server.jar`.

## License
This repository is licensed under the MIT license. All current patches are licensed under the MIT license, but upstream patches may be licensed differently. Please refer to the patch headers for patch-specific licenses.
