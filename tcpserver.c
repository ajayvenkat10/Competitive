#include <unistd.h>
#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>

int main()
{
	int server_fd, sock;
	struct sockaddr_in addr;
	int addrlen = sizeof(addr);
	char buffer[512] = {0};

	server_fd = socket(AF_INET, SOCK_STREAM, 0);

	addr.sin_family = AF_INET;
	addr.sin_addr.s_addr = INADDR_ANY;
	addr.sin_port = htons(8081);

	bind(server_fd, (struct sockaddr *)&addr, addrlen);
	listen(server_fd, 3);
	sock = accept(server_fd, (struct sockaddr *)&addr, (socklen_t*)&addrlen);

	while(recv(sock, buffer, 512, 0))
	{
		printf("Recieved from client: %s\n", buffer);
		bzero(buffer,512);
	}

}
