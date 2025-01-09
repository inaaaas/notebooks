@router.get("/market_offers/details/")
def get_market_offers_with_details(db: Session = Depends(get_db)):
    return db.query(models.MarketOffer, models.Manufacturer).join(
        models.Manufacturer, models.MarketOffer.manufacturer_id == models.Manufacturer.id
    ).all()
