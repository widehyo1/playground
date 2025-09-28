import duckdb
import ipdb

bk = ipdb.set_trace

def main():
    con = duckdb.connect(database=':memory:')

    con.execute("INSTALL httpfs")
    con.execute("LOAD httpfs")

    population = con.read_csv("https://bit.ly/3KoiZR0")

    population.count("*").show()

    # population.to_table("population")
    population_table = con.table("population")

    type(population_table)
    population_table.count("*").show()

    bk()
    (population_table
        .filter('Population > 10000000')
        .project("Country, Population")
        .limit(5)
        .show()
    )

    over_10m = population_table.filter('Population > 10000000')
    (over_10m
        .aggregate("Region, CAST(avg(Population) AS int) as pop")
        .order("pop DESC")
    )
    (over_10m
        .filter('"GDP ($ per capita)" > 10000')
        .count("*")
    )
    over_10m.filter('"GDP ($ per capita)" > 10000').count("*")
    (population_table
        .except_(over_10m)
        .aggregate("""
        Region,
        CAST(avg(Population) AS int) as population,
        count(*)
        """)
    )
    
    # con.execute("SELECT * from population limit 2").fetchall()



if __name__ == "__main__":
    main()
