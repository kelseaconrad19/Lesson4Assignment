class OrdersQueue:
  def __init__(self):
    self.orders = []
    
  def add_order(self, order):
    self.orders.append(order)
  
  def delete_order(self):
    if not self.is_empty():
      return self.orders.pop(0)
    
  def is_empty(self):
    return len(self.orders) == 0
  
  def num_orders(self):
    return len(self.orders) 


  def display_orders(self):
    if self.is_empty():
      print('There are no orders at this time.')
    else:
      print('Orders in the queue:')
      for order in self.orders:
        print(f'- Order: {order['id']}, Timestamp: {order['timestamp']}, Items: {order['items']}')
        
        
order_queue = OrdersQueue()

order_queue.add_order({'id': 1, 'timestamp': "2024-02-13 10:00:00", 'items': 'Hamburger, hotdog, salad'})
order_queue.add_order({'id': 2, 'timestamp': "2024-02-14 10:15:00", 'items': 'Hamburger, hotdog, salad'})
order_queue.add_order({'id': 3, 'timestamp': "2024-02-13 10:35:00", 'items': 'Hamburger, hotdog, salad'})

order_queue.display_orders()

completed_order = order_queue.delete_order()
print(f'Order completed: {completed_order['items']}')

order_queue.display_orders()



class BrowserHistory:
  def __init__(self):
    self.history = []
    
  def add_page(self, page):
    self.history.append(page)
    
  def remove_page(self):
    if not self.is_empty():
      return self.history.pop()
    
  def is_empty(self):
    return len(self.history) == 0
  
  def size(self):
    return len(self.history)
  
  def display_history(self):
    if self.is_empty():
      print("No webpages in the browser's history.")
    else:
      print("Webpages: ")
      for page in self.history:
        print(f'- Page Title: {page['title']}, Url: {page['url']}')
        
browser_history = BrowserHistory()

browser_history.add_page({'title': "Coding Temple", 'url': 'learn.codingtemple.com'})
browser_history.add_page({'title': "Netflix", 'url': 'www.netflix.com'})
browser_history.add_page({'title': "Facebook", 'url': 'www.facebook.com'})


browser_history.display_history()

removed_page = browser_history.remove_page()
print(f"Removed webpage: Title {removed_page['title']}")

browser_history.display_history()

print(browser_history.is_empty())
print(browser_history.size())