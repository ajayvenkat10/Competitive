#include <unistd.h>
#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>

int main()
{
	int server_fd, sock;
	struct sockaddr_in addr, sevadr = {0};
	int addrlen = sizeof(addr), saddrlen = sizeof(sevadr);
	char buffer[512] = {0};
	server_fd = socket(AF_INET, SOCK_DGRAM, 0);

	addr.sin_family = AF_INET;
	addr.sin_addr.s_addr = INADDR_ANY;
	addr.sin_port = htons(8080);
	bind(server_fd, (struct sockaddr *)&addr, addrlen);

	while(recvfrom(server_fd, buffer, 512, 0, &sevadr, &saddrlen))
		printf("Got a UDP dgram from %s : %s\n",  inet_ntoa(sevadr.sin_addr), buffer);
}
