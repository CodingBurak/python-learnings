class ShippingContainer:
  next_serial = 1234
  HEIGHT = 8.5
  WIDTH = 10
  
  @classmethod
  def _get_next_serial(cls): #no need of use of self, do it static.
    result = cls.next_serial
    print("result",result)
    cls.next_serial+= 1
    print("result after static value update", result)
    print("static value update", cls.next_serial)
    return result
  
  def __init__(self, owner_code, contents, length):
    self.owner_code = owner_code,
    self.contents = contents
    self.length = length
    self.serial = ShippingContainer._get_next_serial()
  
  @property
  def volume(self):
    return self._calc_volume()

  def _calc_volume(self):
      return ShippingContainer.HEIGHT * ShippingContainer.WIDTH * self.length
  
  @classmethod
  def create_empty(cls, owner,length, *args, **kwargs):
    return cls(owner, None,length, *args, **kwargs)
  
  @classmethod
  def create_with_items(cls, owner, content, length, *args, **kwargs):
    return cls(owner, list(content), length, *args, **kwargs)
  
    
  def set_serial(self, num):
    ShippingContainer.next_serial = num
  
  
class RefridgeShippingContainer(ShippingContainer):
  
  MAX_CELCIUS = 4.0
  VOLUME_OCCUPIED = 100
  @staticmethod
  def c_to_f(celcius):
    return celcius * 9/5 +32
  
  @staticmethod
  def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9
  
  def __init__(self, owner_code, contents, length,celcius):
    super().__init__(owner_code, contents, length)
    self.celcius = celcius
    
  @property
  def celcius(self):
    return self._celcius
  

  def _calc_volume(self):
    return super()._calc_volume() - RefridgeShippingContainer.VOLUME_OCCUPIED
  
  @celcius.setter
  def celcius(self, val):
    self._set_celsius(val)

  def _set_celsius(self, val):
      if val > RefridgeShippingContainer.MAX_CELCIUS:
        raise ValueError("to high")
      self._celcius = val

  @property
  def fahrenheit(self):
    return RefridgeShippingContainer.c_to_f(self.celcius)
  
  @fahrenheit.setter
  def fahrenheit(self, val):
    self.celcius = RefridgeShippingContainer.f_to_c(val)
  
  
class HeatedShippingContainer(RefridgeShippingContainer):
    
    MIN_CELCIUS = -20.0
    

    def _set_celcius(self, val):
      if val < HeatedShippingContainer.MIN_CELCIUS:
        raise ValueError(" must be lower than {val}".format(val=HeatedShippingContainer.MIN_CELCIUS))
      super()._set_celsius = val