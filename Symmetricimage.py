# t = input("")
class SymmetricImage:

    def countDirections(self,image):

        new_array = []
        for j in range(len(image[0])):
            new_element = ""
            for i in range(len(image)):
                new_element += image[i][j]
            new_array.append(new_element)

        count = 0
        count1 = 0
        ans1 = 0
        ans2 = 0
        if len(image) == 1:
            print(1)

        else:
            for i in range(len(image)):
                if(image[i] == image[i][::-1]):
                    count+=1

            if (count == len(image)):
                ans1 = 1

            else:
                ans1 = 0

            for i in range(len(new_array)):
                if(new_array[i] == new_array[i][::-1]):
                    count1+=1

            if count1 == len(new_array):
                ans2 = 1

            else:
                ans2 = 0

        return (ans1+ans2)
