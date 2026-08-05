
# Detecção de Discurso de Ódio em Imagens com LLaVA

Repositório do meu TCC, desenvolvido como parte do projeto **Radar do Ódio** (CNPq), na Universidade Federal de Sergipe (UFS).

**Autora:** Ellen Vitória Menezes Lima  
**Orientador:** Prof. Hendrik Macedo  
**Instituição:** Universidade Federal de Sergipe (UFS)  

---

## Sobre o projeto

O objetivo foi avaliar se o modelo multimodal **LLaVA-NeXT** consegue detectar discurso de ódio em memes em português e em inglês, e principalmente investigar o quanto a forma como o prompt é formulado muda os resultados.

Foram testadas **40 imagens** (20 neutras e 20 com conteúdo potencialmente odioso) com **três variações de prompt** diferentes, rodando o modelo via Google Colab com GPU T4.

---

## Principais resultados

| Prompt | Abordagem | Accuracy | Precision | Recall | F1 |
|--------|-----------|----------|-----------|--------|----|
| Prompt 1 | Simples e direto | 40,0% | 25,0% | 5,0% | 8,3% |
| Prompt 2 | Estruturado em etapas (role prompting + CoT) | 62,5% | 77,8% | 35,0% | 48,3% |
| Prompt 3 | Prompt 2 + critérios adicionais | 60,0% | 66,7% | 40,0% | 50,0% |

O principal achado: prompts estruturados em etapas produzem resultados expressivamente melhores do que instruções diretas. A diferença de F1 entre o Prompt 1 e o Prompt 2 foi de 8,3% para 48,3%.

---

## Estrutura do repositório

```
├── tcc_llava.ipynb   # Pipeline completo rodando no Google Colab
├── resultados_prompts.xlsx # Resultados dos três prompts organizados por aba
├── imagens/         # Imagens utilizadas para realizar os testes
└── README.md
```

---

## Como rodar

1. Abre o notebook no Google Colab
2. Vai em `Runtime → Change runtime type → T4 GPU`
3. Roda as células em ordem
4. Na célula de upload, sobe as imagens que quiser testar
5. Os resultados são salvos automaticamente em CSV

**Dependências instaladas automaticamente pelo notebook:**
```
transformers accelerate bitsandbytes pillow pandas matplotlib
```

**Modelo usado:**
- `llava-hf/llava-v1.6-mistral-7b-hf` (LLaVA-NeXT Mistral 7B, quantização 4-bit)

---

## Nomenclatura das imagens

As imagens foram organizadas com prefixos que identificam o conteúdo real:
- `meme_c_` → imagens **neutras** (c de *comum*)
- `meme_o_` → imagens **odiosas** (o de *odioso*)

Isso permite que o código identifique o rótulo real de cada imagem automaticamente, sem planilha auxiliar.

---
