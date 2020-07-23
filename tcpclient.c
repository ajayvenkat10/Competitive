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
	char msg[512];
	int sock = socket(AF_INET, SOCK_STREAM, 0);

	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(8081);
	inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr);

	connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr));

	while(1)
	{
		printf("Enter Your Message:");
		scanf("%s", msg);
		send(sock, msg, strlen(msg), 0);
		printf("Sent from client\n");
	}

}
