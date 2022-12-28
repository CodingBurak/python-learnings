class Connection:
  def __init__(self) -> None:
    self.xId =0
    
  def _start_tx(self):
    print("starting tx", self.xId)
    result = self.xId
    self.xId +=1
    return result
  
  def _commit_tx(self, xid):
    print("commiting", xid)
    
  def _rollback_tx(self, xid):
    print("rollback", xid)
    
    
class Transaction:
  def __init__(self, conn:Connection) -> None:
    self.conn = conn
    self.xid = conn._start_tx()
    
  def commit(self):
    self.conn._commit_tx(self.xid)
    
  def rollback(self):
    self.conn._rollback_tx(self.xid)
import contextlib  
@contextlib.contextmanager
def start_tx(conn):
  tx = Transaction(conn=conn)
  try:
    yield tx
  except :
    tx.rollback()
    raise
  tx.commit()
