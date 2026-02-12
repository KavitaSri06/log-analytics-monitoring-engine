from backend.config.dask_config import create_dask_client
import time
def main():
    # Create a Dask client
    client = create_dask_client()
    print(client)
    print(f"Dashboard: {client.dashboard_link}")
    # Your code to perform distributed computations using Dask goes here
    # For example, you can submit tasks to the cluster or use Dask DataFrames
    
    # Don't forget to close the client when you're done
    input("Press Enter to close the Dask client...")
    client.close()
if __name__ == "__main__":
    main()


