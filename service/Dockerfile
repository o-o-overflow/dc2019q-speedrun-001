from ubuntu:18.04
run echo "travis_fold:start:Dapt\033[33;1mservice Dockerfile apt\033[0m" && \
    apt-get -qq update && apt-get install -qq xinetd && \
    echo "\ntravis_fold:end:Dapt\r"


copy speedrun-001 /
run chmod 755 /speedrun-001

run touch /flag && chmod 644 /flag && echo "OOO{Ask any pwner. Any real pwner. It don't matter if you pwn by an inch or a m1L3. pwning's pwning.}" > /flag
copy service.conf /service.conf
copy wrapper /wrapper

expose 31337

cmd ["/usr/sbin/xinetd", "-filelog", "-", "-dontfork", "-f", "/service.conf"]
