# First abstraction test

def test_allocation_to_a_batch_reduces_the_available_quantity():
    batch = Batch("batch-001","SMALL-TABLE",qty=20, eta=date.today())
    line = OrderLine("order-ref","SMALL-TABLE")
    batch.allocate(line)
    assert batch.available_quantity == 18

# today() = dzisiejsza data 
# użycie funkcji allocate to jest hermetyzacja

# Tworzy automatycznie __init__, __repr__, __eq__
# fronzen = immutable 
@dataclass(frozen=True)
class OrderLine: 
    orderid: str 
    sku: str
    qty: int 

class Batch:
    def __init__(self, ref: str, sku:str, qty: int, eta: Optional[date]):
        self.reference = ref 
        self.sku = sku 
        self.eta = eta 
        self.avaiable_quantity = qty 
    def allocate(self, line: OrderLine):
        self.available_quantity -= line.qty


# TESTS

def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch("batch-001", sku, batch_qty, eta=date.today()),
        OrderLine("order-123", sku, line_qty)
    )
def test_can_allocate_if_available_greater_than_required():
    large_batch, small_line = make_batch_and_line("ELEGANT-LAMP",20,2)
    assert large_batch.can_allocate(small_line)

#

class Batch:
    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set()  # type: Set[OrderLine]

    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.q
    
    # property - w locie - robi to jednocześnie, natychmiast


    class Batch:
        def __eq__(self, other):
            if not isinstance(other, Batch):
                return False
            return other.reference == self.reference

        def __hash__(self):
            return hash(self.reference)
    # equality - sprawdza adresy w pamięci RAM, pozwala narzucić ramy
    # hash - przekształca stan obiektu w stałą liczbę całkowitą, niezbędne do set i dict
    # jeśli eq jest równe to hash musi zwrócić to samo
        def __gt__(self, other):
            if self.eta is None:
                return False
            if other.eta is None:
                return True
            return self.eta > other.eta
    # greater than nadpisuje zachowanie operatora 
