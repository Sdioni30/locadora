from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, registry


table_registry = registry()


@table_registry.mapped_as_dataclass
class Jogos:
    __tablename__ = 'jogos'

    codigo_de_barras: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    classificacao_idade : Mapped[int] = mapped_column(nullable=False)
    preco: Mapped[float] = mapped_column(nullable=False)
    disponivel: Mapped[bool] = mapped_column(Boolean, default=True)