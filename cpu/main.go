package cpu

import (
	"bufio"
	"os/exec"
	"strconv"
	"strings"
)

func parseRang(str string) []int64 {

	var res []int64
	tmp := strings.Split(strings.Replace(str, " ", "", -1), ",")
	for _, tp := range tmp {
		if strings.Contains(tp, "-") {
			subtmp := strings.Split(tp, "-")
			start, err := strconv.ParseInt(subtmp[0], 10, 64)
			if err != nil {
				panic(err)
			}
			end, err := strconv.ParseInt(subtmp[1], 10, 64)
			if err != nil {
				panic(err)
			}
			for m := start; m <= end; m++ {
				res = append(res, m)
			}
			continue
		}
		num, err := strconv.ParseInt(tp, 10, 64)
		if err != nil {
			panic(err)
		}
		res = append(res, num)
	}
	return res
}

func GetOnlineNum() int {
	var num int
	cmd := exec.Command("cat", "/sys/devices/system/cpu/online")
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		panic(err)
	}
	cmd.Start()
	reader := bufio.NewReader(stdout)
	for {
		line, _ := reader.ReadString('\n')
		num = len(parseRang(strings.Replace(line, "\n", "", -1)))
		break
	}
	cmd.Wait()
	return num
}
