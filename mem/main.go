package mem

import (
	"bufio"
	"io"
	"os/exec"
	"strconv"
	"strings"
)

func GetTotalSize() float64 {
	var size float64
	cmd := exec.Command("cat", "/proc/meminfo")
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		panic(err)
	}
	cmd.Start()
	reader := bufio.NewReader(stdout)

	for {
		line, err := reader.ReadString('\n')
		if err != nil || io.EOF == err {
			break
		}
		if strings.Contains(line, "MemTotal:") {
			str := strings.Split(line, " ")
			sizeInt, err := strconv.ParseInt(str[len(str)-2], 10, 64)
			if err != nil {
				panic(err)
			}
			size = 0.5 + float64(sizeInt)/(1024.0*1024.0)
			break
		}
	}
	cmd.Wait()
	return size
}
