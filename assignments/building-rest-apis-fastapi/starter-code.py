from typing import List

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Products API")


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    in_stock: bool = True


class Product(ProductCreate):
    id: int


# Armazenamento em memória para prática da atividade.
products: List[Product] = []


@app.get("/")
def health_check():
    return {"status": "ok", "service": "products-api"}


@app.get("/products", response_model=List[Product])
def list_products():
    # TODO: retornar a lista de produtos.
    return products


@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(payload: ProductCreate):
    # TODO: criar produto com ID incremental e salvar em memória.
    product = Product(id=len(products) + 1, **payload.model_dump())
    products.append(product)
    return product


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    # TODO: buscar produto por ID e retornar 404 se não existir.
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
