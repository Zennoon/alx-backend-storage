-- Creates a trigger on the order table so that when an order is
-- made, the ordered item's quantity is decremented from the items
-- table
DELIMITER $$
CREATE TRIGGER decr_items AFTER INSERT ON orders FOR EACH ROW
BEGIN
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
END $$
DELIMITER ;
