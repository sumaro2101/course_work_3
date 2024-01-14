from src.data.data_manager import File
from collections import namedtuple

class FileSummary(File):
    _summary = namedtuple('Summary', ['time', 'description', 'from_', 'to', 'amount', 'valute'])
    _summary.__new__.__defaults__ = (None, None, None, None, None, None)
    
    @classmethod
    def get_formated(cls, time):
        if len(time) <= 2:
            return time.rjust(2, '0')
        if len(time) <= 4:
            return time.rjust(4, '0')
        
    @classmethod
    def make_time(cls, time=None):
        if time is None:
            return None
        result = time.split("T")[0].split("-")
        return ".".join(result[::-1])
        
    @classmethod 
    def make_mask_account(cls, number=None):
        if number is None:
            return None
        return "".join(["**", number[-4:]])
        
        
    @classmethod
    def make_mask_visa(cls, card=None, digits_spase=4, mask_char='*'):
        
        if card is None:
            return None
        
        if len(card.split(" ")) == 2:
            
            name, number = card.split(' ')
            if name == "Счет":
                
                result = cls.make_mask_account(number)
                return f"{name} {result}"
            
            number = "".join([number[:6], mask_char * len(number[6:-4]), number[-4:]])
            result = " ".join(map("".join, zip(*[iter(number)] * digits_spase)))
            
            return f"{name} {result}"

        if len(card.split(" ")) == 3:
            
            name_visa, type_visa, number = card.split(' ')
            number = "".join([number[:6], mask_char * len(number[6:-4]), number[-4:]])
            result = " ".join(map("".join, zip(*[iter(number)] * digits_spase)))
            
            return f'{name_visa} {type_visa} {result}'
    
    @property
    def result(self):
        return self.__result
    
    @result.setter
    def result(self, count_files):
        self.__result = [self._summary(time=self.make_time(item.get('date')),
                                        description=item.get('description'),
                                        from_=self.make_mask_visa(item.get('from')),
                                        to=self.make_mask_account(item.get('to')),
                                        amount=float(item.get('operationAmount').get('amount', None)),
                                        valute=item.get('operationAmount').get('currency', None).get('name', None))
                         for item in self.give_sort_file(self.open_file, count_files)]
 
                
                