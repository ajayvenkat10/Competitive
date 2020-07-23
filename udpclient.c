#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#include <arpa/inet.h>
#include <unistd.h>

int main()
{
	struct sockaddr_in serv_addr = {0};
	char *msg = "Hey From Client!";
	int sock = socket(AF_INET, SOCK_DGRAM, 0);
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(8080);
	inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr);

	while(sendto(sock, msg, strlen(msg), 0, &serv_addr, sizeof(serv_addr))!= -1)
		sleep(2);

}
