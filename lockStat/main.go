package lockStat

import (
	"bufio"
	"io"
	"io/ioutil"
	"os"
	"os/exec"
)

func Start() {
	err := ioutil.WriteFile("/proc/sys/kernel/lock_stat", []byte("0"), os.ModeAppend)
	if err != nil {
		panic(err)
	}
	err = ioutil.WriteFile("/proc/lock_stat", []byte("0"), os.ModeAppend)
	if err != nil {
		panic(err)
	}
	err = ioutil.WriteFile("/proc/sys/kernel/lock_stat", []byte("1"), os.ModeAppend)
	if err != nil {
		panic(err)
	}
}

func Stop() {
	err := ioutil.WriteFile("/proc/sys/kernel/lock_stat", []byte("0"), os.ModeAppend)
	if err != nil {
		panic(err)
	}
}

func GetLockStat(outputfile string) {
	var cmd *exec.Cmd
	fp, err := os.OpenFile(outputfile, os.O_CREATE|os.O_TRUNC|os.O_RDWR, os.ModePerm|os.ModeTemporary)
	cmd = exec.Command("cat", "/proc/lock_stat")
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		panic(err)
	}
	err = cmd.Start()
	if err != nil {
		panic(err)
	}
	reader := bufio.NewReader(stdout)
	for {
		line, err := reader.ReadString('\n')
		fp.WriteString(line)
		if err != nil || io.EOF == err {
			break
		}
	}
	cmd.Wait()
	fp.Close()
}
