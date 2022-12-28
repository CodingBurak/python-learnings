from pprint import pprint
class Aircraft:
  
  def __init__(self, registration, model, num_rows, num_seats_per_row) -> None:
    self._registration = registration
    self._model = model
    self._num_rows = num_rows
    self._num_seats_per_row = num_seats_per_row
    
  def registration(self):
    return self._registration
  
  def model(self):
    return self._model
  def set_model(self, model):
    self._model = model
  
 

class Airbus(Aircraft):
   def seating_plan(self):
    return (range(1, self._num_rows +1), "ABCDEFGHJK"[:self._num_seats_per_row])
  

class Boeing(Aircraft):
   def seating_plan(self):
    return (range(1, self._num_rows +1), "ABCDEFGHJK"[:self._num_seats_per_row])
  

class Flight:
  
  def __init__(self, number, aircraft: Aircraft) -> None:
    self._number = number
    self._aircraft = aircraft
    rows, seats = aircraft.seating_plan()
    self._seating = [None] + [{letters: None for letters in seats} for _ in rows]
  
  def get_airline(self):
    return self._number[:2]
  
  def number(self):
    return self._number
  
  def aircraft_model(self):
    return self._aircraft.model()
  
  def _parse_seat(self, seat):
    rows, seat_letters = self._aircraft.seating_plan()
    
    letter = seat[-1]
    row = int(seat[:-1])
    if letter not in seat_letters:
      raise ValueError("invalid seat")
    if row not in rows:
      raise ValueError("non existing row number")
    return row,letter
  
  def assign_seat(self, seat, passenger):
    row, letter = self._parse_seat(seat)
    self._seating[row][letter] = passenger
    pprint(self._seating)
    
  def num_available_seats(self):
    return sum(sum(1 for seatStr in row.values() if seatStr is None) for row in self._seating if row is not None)
  
  def make_boarding_cards(self, log_card_printer):
    for passenger, seat in self.passenger_seats():
      print("yield!!")
      log_card_printer(passenger, seat, self.number(), self.aircraft_model())
      
  def passenger_seats(self):
    row_numbers, seat_letters = self._aircraft.seating_plan()
    for number in row_numbers:
      for letter in seat_letters:
        if self._seating[number][letter] is not None:
          print("about to yield")
          yield self._seating[number][letter], str(number)+letter
          
          
    
  def relocate_passenger(self, from_seat, target_seat):
    from_row, from_letter = self._parse_seat(from_seat)
    if self._seating[from_row][from_letter] is None:
      raise ValueError("no passenger on this seat")
    to_row, to_letter = self._parse_seat(target_seat)
    self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
    self._seating[from_row][from_letter] = None
    pprint(self._seating)
    
def log_card_printer(passenger, seat, flight_number, aircraft):
  output = ''' | Name: {0}
               Flight: {1}
               Seat: {2}
               Aircraft: {3}
               |'''.format(passenger, flight_number, seat, aircraft)
  
  banner = '+' + "-" * (len(output) - 2) + "+"
  border = '|' + "." * (len(output) - 2) + "|"
  layout = [banner, border, output, banner]
  card = '''
          '''.join(layout)
  print(card)
  print()
  
      
def generate_flight():
  f = Flight("BA123", Aircraft("G-123", "Airbus A390", num_rows=22, num_seats_per_row=4))
  f.assign_seat("12A", "Burak")
  f.assign_seat("11A", "Burak")
  f.assign_seat("2A", "Burak")
  f.assign_seat("4A", "Burak")
  f.assign_seat("5A", "Burak")
  f.assign_seat("12A", "Burak")
  return f
  

    
