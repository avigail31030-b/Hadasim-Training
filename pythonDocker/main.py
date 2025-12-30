import docker

def main():

    print("STARTING PYTHON DOCKER SCRIPT")

    client = docker.from_env()

    container = client.containers.run(
        image = "busybox:latest",
        command = ["sleep", "300"],
        detach = True,
    )

    try:
        result = container.exec_run(["hostname"])

        hostname = result.output.decode("utf-8").strip()

        print(f"Container ID: {container.short_id}")
        print(f"Hostname: {hostname}")

    finally:
        container.stop()
        container.remove()

if __name__ == "__main__":
    main()