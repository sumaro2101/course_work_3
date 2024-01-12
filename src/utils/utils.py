from src.data.data_manager import File
from collections import namedtuple

class FileSummary(File):
    __summary = namedtuple('Summary', ['time', 'description', 'from_', 'to', 'amount', 'valute'])
    __summary.__new__.__defaults__ = (None, None, None, None, None, None)

    @property
    def result(self):
        return self.__result
    
    @result.setter
    def result(self, count_files):
        self.__result = []
        for date_ in self.open_file:
            if len(self.result) == count_files:
                break
            if date_["state"] == "CANCELED":
                continue
            else:
                self.__result.append(self.__summary(time=date_.get('date').split("T")[0],\
                                                    description=date_.get('description'),\
                                                    from_=date_.get('from'),\
                                                    to=date_.get('to'),\
                                                    amount=float(date_.get('operationAmount').get('amount')),\
                                                    valute=date_.get('operationAmount').get('currency').get('name')))
                