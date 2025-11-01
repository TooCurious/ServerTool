from fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import Optional


mcp = FastMCP("Personal Information Detection", host="0.0.0.0", port=5005)



ORDERS = [
    {"order_id": "A123", "status": "Shipped", "eta_days": 2},
    {"order_id": "B456", "status": "Processing", "eta_days": 4},
    {"order_id": "C789", "status": "Delivered", "eta_days": 0},
    {"order_id": "D234", "status": "Pending Payment", "eta_days": None},
    {"order_id": "E567", "status": "Packed", "eta_days": 3},
    {"order_id": "F890", "status": "Shipped", "eta_days": 1},
    {"order_id": "G135", "status": "On Hold", "eta_days": None},
    {"order_id": "H246", "status": "Processing", "eta_days": 5},
    {"order_id": "I357", "status": "Delivered", "eta_days": 0},
    {"order_id": "J468", "status": "Cancelled", "eta_days": None},
    {"order_id": "K579", "status": "Shipped", "eta_days": 2},
    {"order_id": "L680", "status": "Label Created", "eta_days": 6},
    {"order_id": "M791", "status": "Processing", "eta_days": 4},
    {"order_id": "N802", "status": "Delivered", "eta_days": 0},
    {"order_id": "O913", "status": "Packed", "eta_days": 3}
]

class OrderRequest(BaseModel):
    order_id: str = Field(description="The unique identifier of the order.")


class OrderResponse(BaseModel):
    order_id: str
    status: str
    eta_days: Optional[int]



@mcp.tool()
def get_order_status_tool(order_id: str) -> OrderResponse:
    """
    Инструмент (tool) для получения статуса заказа.
    """
    order = next((o for o in ORDERS if o["order_id"] == order_id), None)
    if order:
        return OrderResponse(
            order_id=order["order_id"],
            status=order["status"],
            eta_days=order["eta_days"]
        )
    else:
        raise ValueError(f"Order with ID {order_id} not found.")


if __name__ == "__main__":
    mcp.run(transport="streamable-http")