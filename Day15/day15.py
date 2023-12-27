from day import Day

class Day15(Day):

    def __init__(self):
        Day.__init__(self, 15)


    class Lens:

        def __init__(self, label, focal_length):
            self.label = label
            self.focal_length = focal_length
            self.next_lens = None


    class Box:

        def __init__(self, num):
            self.box_num = num
            self.root_lens = None

        def add_lens(self, lens):
            if self.root_lens is None:
                self.root_lens = lens
                return

            if self.root_lens.label == lens.label:
                self.root_lens.focal_length = lens.focal_length
                return
            
            current = self.root_lens
            next_lens = current.next_lens
            while next_lens is not None:
                if next_lens.label == lens.label:
                    next_lens.focal_length = lens.focal_length
                    return
                current = next_lens
                next_lens = current.next_lens

            current.next_lens = lens
            
        def remove_lens(self, label):
            current = self.root_lens
            if current is None:
                return

            if current.label == label:
                self.root_lens = current.next_lens
                return

            next_lens = current.next_lens
            while next_lens is not None:
                if next_lens.label == label:
                    current.next_lens = next_lens.next_lens
                    return
                current = next_lens
                next_lens = current.next_lens

        def get_focusing_power(self):
            power = 0
            box_num = self.box_num + 1
            slot_num = 1
            current = self.root_lens
            while current is not None:
                power += box_num * slot_num * current.focal_length
                slot_num += 1
                current = current.next_lens
            return power

        def __str__(self):
            if self.root_lens is None:
                return ''

            as_str = f'Box {self.box_num}: '
            current = self.root_lens
            while current is not None:
                as_str += f'[{current.label} {current.focal_length}] '
                current = current.next_lens
            return as_str + '\n'


    def remove_lens(self, boxes, label):
        box_num = self.get_hash(label)
        boxes[box_num].remove_lens(label)


    def add_lens(self, boxes, label, focal_length):
        box_num = self.get_hash(label)
        lens = self.Lens(label, focal_length)
        boxes[box_num].add_lens(lens)


    def get_hash(self, value):
        current = 0
        for char in value:
            num = ord(char)
            current += num
            current *= 17
            current = current % 256
        return current


    def get_solution_a(self, input_data):
        '''
        Determine the ASCII code for the current character of the string.
        Increase the current value by the ASCII code you just determined.
        Set the current value to itself multiplied by 17.
        Set the current value to the remainder of dividing itself by 256.
        '''
        total_sum = 0
        unhashed_values = input_data[0].split(',')
        for unhashed in unhashed_values:
            total_sum += self.get_hash(unhashed)
        return total_sum


    def get_solution_b(self, input_data):
        boxes = []
        for i in range(0, 256):
            boxes.append(self.Box(i))

        sequences = input_data[0].split(',')
        for sequence in sequences:
            if sequence[-1] == '-':
                self.remove_lens(boxes, sequence[:-1])
            else:
                values = sequence.split('=')
                self.add_lens(boxes, values[0], int(values[1]))

        total_power = 0
        for box in boxes:
            total_power += box.get_focusing_power()
        
        return total_power
        
    def get_expected_a(self):
        return 1320

    def get_expected_b(self):
        return 145