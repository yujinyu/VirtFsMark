package cntrs

import (
	"fmt"
	"io"
	"os"

	"bufio"
	"github.com/docker/docker/api/types"
	"github.com/docker/docker/api/types/container"
	"github.com/docker/docker/client"
	"golang.org/x/net/context"
	"os/exec"
)

func PullImage(imageName string) {
	clt, err := client.NewEnvClient()
	out, err := clt.ImagePull(context.Background(), imageName, types.ImagePullOptions{})
	if err != nil {
		panic(err)
	}
	defer out.Close()
	io.Copy(os.Stdout, out)
}

func BuildImage1(path2df string, newImageName string) {
	clt, err := client.NewEnvClient()
	if err != nil {
		panic(err)
	}
	_, err = clt.ImageBuild(context.Background(), nil, types.ImageBuildOptions{
		Dockerfile: path2df,
		Tags:       []string{newImageName},
	})
	if err != nil {
		panic(err)
	}
}
func BuildImage2(path2df string, newImageName string) {
	cmd := exec.Command("docker", "build ./ -t %s", path2df, newImageName)
	cmd.Dir = path2df
	fmt.Println("A")
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		panic(err)
	}
	cmd.Start()
	fmt.Println("B")
	reader := bufio.NewReader(stdout)
	for {
		line, err := reader.ReadString('\n')
		fmt.Println(line)
		if err != nil || io.EOF == err {
			break
		}
	}
	cmd.Wait()
}

func CreateContainer(imageName string, hostName string, cntrName string, vol map[string]struct{}, cmd []string, workingDir string) {
	ctx := context.Background()
	clt, err := client.NewEnvClient()
	if err != nil {
		panic(err)
	}

	images, err := clt.ImageSearch(ctx, imageName, types.ImageSearchOptions{})
	if err != nil {
		panic(err)
	}
	if images == nil {
		fmt.Println("Image %s is unavailable", imageName)
		os.Exit(-1)
	}
	resp, err := clt.ContainerCreate(ctx, &container.Config{
		Hostname: hostName,
		Cmd:      cmd,
		Image:    imageName,
		Volumes:  vol,
	}, nil, nil, cntrName)
	if err != nil {
		panic(err)
	}

	if err := clt.ContainerStart(ctx, resp.ID, types.ContainerStartOptions{}); err != nil {
		panic(err)
	}
	fmt.Println(resp.ID)
}

func DeleteContainers(Force bool) {
	cli, err := client.NewEnvClient()
	if err != nil {
		panic(err)
	}

	containers, err := cli.ContainerList(context.Background(), types.ContainerListOptions{All: true})
	if err != nil {
		panic(err)
	}

	for _, cntr := range containers {
		if cntr.Status == "Running" {
			if err := cli.ContainerStop(context.Background(), cntr.ID, nil); err != nil {
				panic(err)
			}
		}
		cli.ContainerRemove(context.Background(), cntr.ID, types.ContainerRemoveOptions{Force: Force})
	}
}
