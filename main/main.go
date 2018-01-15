package main

import (
	"fmt"

	"os"
	"path"

	"log"

	"cntrMarks/cntrs"
)

func main() {
	currentWorkDir, err := os.Getwd()
	imageName := "cntrmarks:test"
	if err != nil {
		log.Fatal(err)
	}

	path2df := path.Join(currentWorkDir, "image_built/")
	os.Chdir(path2df)
	fmt.Println(os.Getwd())
	cntrs.BuildImage2(path2df, imageName)

	//lockStat.Start()
	//fmt.Println(mem.GetTotalSize())
	//fmt.Println(cpu.GetOnlineNum())
	//lockStat.Stop()

	//resDir := path.Join(currentWorkDir, "result")
	//err = os.Mkdir(resDir, os.ModePerm)
	//if err != nil {
	//	lockStat.GetLockStat(path.Join(resDir, "resultFile"))
	//}
}
