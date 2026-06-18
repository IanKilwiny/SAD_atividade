"""
Módulo de utilidades para o dashboard de desempenho de estudantes
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple


class DataAnalysis:
    """Classe com funções utilitárias para análise de dados"""
    
    @staticmethod
    def calculate_percentile(series: pd.Series, percentile: float) -> float:
        """Calcula o percentil de uma série"""
        return np.percentile(series, percentile)
    
    @staticmethod
    def calculate_improvement(before: float, after: float) -> float:
        """Calcula a melhoria percentual entre dois valores"""
        if before == 0:
            return 0
        return ((after - before) / before) * 100
    
    @staticmethod
    def get_performance_level(score: float) -> str:
        """Classifica o desempenho baseado na nota"""
        if score >= 80:
            return "Excelente"
        elif score >= 70:
            return "Bom"
        elif score >= 60:
            return "Satisfatório"
        elif score >= 50:
            return "Aceitável"
        else:
            return "Insuficiente"
    
    @staticmethod
    def get_group_statistics(df: pd.DataFrame, group_column: str, 
                            value_columns: List[str]) -> Dict:
        """Calcula estatísticas por grupo"""
        stats = {}
        for column in value_columns:
            stats[column] = {
                'mean': df.groupby(group_column)[column].mean(),
                'std': df.groupby(group_column)[column].std(),
                'min': df.groupby(group_column)[column].min(),
                'max': df.groupby(group_column)[column].max(),
                'median': df.groupby(group_column)[column].median(),
            }
        return stats
    
    @staticmethod
    def get_top_performers(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
        """Retorna os top N estudantes com melhor desempenho geral"""
        df_copy = df.copy()
        df_copy['average_score'] = (
            df_copy['math score'] + 
            df_copy['reading score'] + 
            df_copy['writing score']
        ) / 3
        return df_copy.nlargest(n, 'average_score')
    
    @staticmethod
    def get_students_needing_support(df: pd.DataFrame, threshold: float = 50) -> pd.DataFrame:
        """Retorna estudantes que precisam de apoio (nota média abaixo do limiar)"""
        df_copy = df.copy()
        df_copy['average_score'] = (
            df_copy['math score'] + 
            df_copy['reading score'] + 
            df_copy['writing score']
        ) / 3
        return df_copy[df_copy['average_score'] < threshold]
    
    @staticmethod
    def get_correlation_insights(df: pd.DataFrame, 
                                 col1: str, col2: str) -> Tuple[float, str]:
        """Retorna correlação e uma interpretação"""
        corr = df[col1].corr(df[col2])
        
        if abs(corr) >= 0.7:
            strength = "forte"
        elif abs(corr) >= 0.4:
            strength = "moderada"
        else:
            strength = "fraca"
        
        direction = "positiva" if corr > 0 else "negativa"
        
        interpretation = f"Correlação {strength} {direction} ({corr:.3f})"
        return corr, interpretation


def prepare_data_for_export(df: pd.DataFrame) -> pd.DataFrame:
    """Prepara dados para exportação"""
    df_export = df.copy()
    df_export['average_score'] = (
        df_export['math score'] + 
        df_export['reading score'] + 
        df_export['writing score']
    ) / 3
    df_export['performance_level'] = df_export['average_score'].apply(
        DataAnalysis.get_performance_level
    )
    return df_export


def get_summary_statistics(df: pd.DataFrame) -> Dict:
    """Retorna um resumo estatístico dos dados"""
    return {
        'total_students': len(df),
        'unique_genders': df['gender'].nunique(),
        'unique_ethnicities': df['race/ethnicity'].nunique(),
        'math_mean': df['math score'].mean(),
        'math_median': df['math score'].median(),
        'math_std': df['math score'].std(),
        'reading_mean': df['reading score'].mean(),
        'reading_median': df['reading score'].median(),
        'reading_std': df['reading score'].std(),
        'writing_mean': df['writing score'].mean(),
        'writing_median': df['writing score'].median(),
        'writing_std': df['writing score'].std(),
    }
