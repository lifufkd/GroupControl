#####################################
#            Created by             #
#                SBR                #
#               zzsxd               #
#####################################
#####################################


class TempUserData:
    def __init__(self):
        super(TempUserData, self).__init__()
        self.__user_data = {}

    def temp_data(self, user_id):
        if user_id not in self.__user_data.keys():
            self.__user_data.update({user_id: [None]}) # 1 - status, 2 - m
        return self.__user_data